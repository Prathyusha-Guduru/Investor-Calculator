plotForm = document.getElementById('plotForm')
plotForm.addEventListener(('submit'),(e)=>{
	e.preventDefault()
	console.log('method working');
	console.log(`maturity value is ${maturityValue} and investment is ${investment}`);
	console.log('RANDOM RANDOM STUFF');
	Highcharts.chart("container", {
		chart: {
		  type: "pie",
		  options3d: {
			enabled: true,
			alpha: 45
		  },
		  backgroundColor: "#e6e7ee"
		},
  title: {
    text: ''
  },
		plotOptions: {
		  pie: {
			innerSize: 100,
			depth: 45
		  }
		},
		series: [
		  {
			name: "Delivered amount",
			data: [
					['Maturity Value (INR)',maturityValue],
					['Investmented Amount (INR)',investment]
			]
		  }
		]
	  });
			
})