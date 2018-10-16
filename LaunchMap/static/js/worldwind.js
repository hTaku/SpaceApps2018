class NasaWorldWind{
	constructor(canvasId){
		this.wwd = new WorldWind.WorldWindow(canvasId);

		this.layers = [
			{layer: new WorldWind.BMNGOneImageLayer(),           enabled: true},
			{layer: new WorldWind.BMNGLandsatLayer(),            enabled: true},
//			{layer: new WorldWind.CompassLayer(),                enabled: true},
			{layer: new WorldWind.CoordinatesDisplayLayer(this.wwd), enabled: true},
			{layer: new WorldWind.ViewControlsLayer(this.wwd),       enabled: true},
		];

		this.layers.forEach(function(layer){
			layer.layer.enabled = layer.enabled;
			this.addLayer(layer.layer);
		}, this.wwd);
		
		this.renderLayer = new WorldWind.RenderableLayer('renderLayer');
		this.wwd.addLayer(this.renderLayer);
		
		this.positions = new Map();
	}

	createPosition(id, lat, lon, name, image){
		const placemarkAttributes = new WorldWind.PlacemarkAttributes(null);

		placemarkAttributes.imageOffset = new WorldWind.Offset(
			WorldWind.OFFSET_FRACTION, 0.3,
			WorldWind.OFFSET_FRACTION, 0.0);

		placemarkAttributes.labelAttributes.color = WorldWind.Color.YELLOW;
		placemarkAttributes.labelAttributes.offset = new WorldWind.Offset(
					WorldWind.OFFSET_FRACTION, 0.5,
					WorldWind.OFFSET_FRACTION, 1.0);

		placemarkAttributes.imageSource = image;

		const position = new WorldWind.Position(lat, lon, 100);
		const placemark = new WorldWind.Placemark(position, false, placemarkAttributes);
/*
		placemark.label = name + "\n" +
			"Lat " + placemark.position.latitude.toPrecision(4).toString() + "\n" +
			"Lon " + placemark.position.longitude.toPrecision(5).toString();
*/
		placemark.label = name;

		placemark.alwaysOnTop = true;

		placemark.pickDelegate = new Object();
		placemark.pickDelegate.id = id;

		return placemark;
	}
	
	addPins(jsonData){
		jsonData.forEach(function(data){
			const placemark = this.createPosition(data.id, data.lat, data.lon, data.name, data.image);
			this.positions.set(data.id, {'id': data.id, 'data': data, 'placemark': placemark});
		}, this);
	}

	showPoint(lat, lon){
		new WorldWind.GoToAnimator(this.wwd).goTo(new WorldWind.Position(lat, lon, 40000));
	}

	draw(){
		this.positions.forEach(function(position){
			this.renderLayer.addRenderable(position.placemark);
		}, this);
	}

	addEventListener(action, handler){
		if(action == 'pinclick') {
			const worldwind = this.wwd;
			const datas = this.positions;
			this.wwd.addEventListener('click', function(event){
				const x = event.clientX, y = event.clientY;

				let redrawRequired = false;
				const pickList = worldwind.pick(worldwind.canvasCoordinates(x, y));
				if(pickList.objects.length > 0) {
					redrawRequired = true;

					for(let i = 0; i < pickList.objects.length - 1; i++) {
						const pickObj = pickList.objects[i];
						if(!pickObj.isTrrain) {
							const id = pickObj.userObject.id;
							console.log('pickObj.userObject=' + id);
							const pickData = datas.get(id);
							console.log("data Object:" + pickData.data);
							handler(pickObj, pickData.data, x, y);
							break;
						}
					}
				}
				if(redrawRequired) {
					worldwind.redraw();
				}
			});
		}
	}
}

