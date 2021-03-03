plot = document.getElementById('showPlot')
console.log(plot);

Highcharts.chart("container", {
	chart: {
	  type: "pie",
	  options3d: {
		enabled: true,
		alpha: 45
	  },
	  backgroundColor: "#f6c065"
	},
	title: {
	  text: "Contents of Highsoft's weekly fruit delivery"
	},
	subtitle: {
	  text: "3D donut in Highcharts"
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
				['Final Amount',10000],
				['Investment',5000]
		]
	  }
	]
  });
  