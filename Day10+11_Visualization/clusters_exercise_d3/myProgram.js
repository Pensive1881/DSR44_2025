var url = "https://raw.githubusercontent.com/chumo/Data2Serve/master/transition_clusters.csv";

function loadAndParse(data) {

  d3.select('svg')
    .selectAll('circle')
    .data(data)
    .join('circle')
    .attr('cx', d => d.Xi)
    .attr('cy', d => d.Yi)
    .attr('r', 5)
    .attr('fill', d => d.color)
    .transition()
    .duration(5000)
    .attr('cx', d => d.Xf)
    .attr('cy', d => d.Yf);

  d3.selectAll('circle').on('mouseover', function(){
    d3.select(this).transition().attr('r', 20);
  })

  d3.selectAll('circle').on('mouseout', function(){
    d3.select(this).transition().attr('r', 5);
  })

}


d3.csv(url, d3.autoType).then(function(data){
  loadAndParse(data);
})
