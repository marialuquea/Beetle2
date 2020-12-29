function slider(id) {
    var index = id.split("_");
    var x = document.getElementById(id).value;
    document.getElementById('answer_' + index[1]).innerHTML =  x;
}

var ready = false;

function checkSliders() {
  // Geometry and loads
  var l1 = document.getElementById('answer_1').innerText;
  var l2 = document.getElementById('answer_2').innerText;
  var l3 = document.getElementById('answer_4').innerHTML;
  var l4 = document.getElementById('answer_5').innerHTML;
  var l5 = document.getElementById('answer_6').innerHTML;
  var l6 = document.getElementById('answer_7').innerText;
  var l7 = document.getElementById('answer_8').innerText;
  var l8 = document.getElementById('answer_10').innerHTML;
  var l9 = document.getElementById('answer_11').innerHTML;
  
  if (l1 == '' || l2 == '' || l3 == '' || l4 == '' || l5 == ''|| l6 == '' || l7 == '' || l8 == '' || l9 == '') 
  {
    alert("You must select values for all the inputs.");
    ready = false;
  }
  else 
  {
    var l10 = document.getElementById('distribution_select').value;
    if (l10 == 'Triangular') 
    {
      var l11 = document.getElementById('answer_12').innerHTML; // triangle
      var l12 = document.getElementById('answer_13').innerHTML;
      var l13 = document.getElementById('answer_14').innerHTML;
      if (l11 != '' && l12 != '' && l13 != '')
      { 
        if (parseFloat(l11) <= parseFloat(l12) && parseFloat(l13) <= parseFloat(l12)){ ready = true;  }
        else {alert("Distribution should be Lower bound <= Mode <= Upper bound"); ready = false;}
      }
      else{ alert("You must select values for all the inputs."); ready = false;}
    }
    if (l10 == 'Uniform') 
    {
      var l14 = document.getElementById('answer_15').innerHTML; // uniform
      var l15 = document.getElementById('answer_16').innerHTML;
      if (l14 != '' && l15 != ''){ 
        if (parseFloat(l14) <= parseFloat(l15)) { ready = true; }
        else {alert("Distribution should be Lower bound <= Upper bound");}
      }
      else{ alert("You must select values for all the inputs."); ready = false;}
    }
    if (l10 == 'Gaussian') 
    {
      var mean = document.getElementById('answer_17').innerHTML; // gaussian mean
      var std = document.getElementById('answer_18').innerHTML; // st dev
      if (mean != '' && std != '') { 
        if ((mean - (3 * std)) >= 0) { ready = true;  }
        else  {  alert("Input values for Gaussian distribution not valid. Select a higher mean or a lower standard deviation."); }
      }
      else { alert("You must select values for all the inputs."); ready = false;  }
    }
  }
}

function plot_histogram(data)
{
  if (ready == true)
  {
    if (data == ''){
      alert('An error has occured and there is no data to display in the histogram.');
    }
    var res = String(data).split(",");
    var inputs = []
    for (i = 0; i < res.length; i++){
      inputs.push(parseFloat(res[i]))
    }

    // plot inputs 
    histogram(inputs)
  }
}

function histogram(inputs)
{
  var trace = {
      x: inputs,
      type: 'histogram',
      histnorm: 'probability',
      marker: {
        color: '#7F39FB',
      }
  };
  var data = [trace];
  var layout = {
    xaxis: {
      title: 'Embodied carbon [kgCO<sub>2</sub>e]',
      titlefont: {
        family: 'Arial, sans-serif',
        size: 18,
        color: 'lightgrey'
      }
    },
    yaxis: {
      title: 'Probability',
      titlefont: {
        family: 'Arial, sans-serif',
        size: 18,
        color: 'lightgrey'
      }
    }
  };

  Plotly.newPlot('hg', data, layout);
  ready = false;
}