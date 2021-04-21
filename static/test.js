document.addEventListener("DOMContentLoaded", function(event) { 
  var buttonsWanted = 10;
  var doc = document;
  var docFrag = document.createDocumentFragment();

  for(var x = 0; x < buttonsWanted; x++){
    var button = doc.createElement('button');
    button.setAttribute('text', 'yourtext');
    docFrag.appendChild(button);
  }

  doc.getElementById('container').appendChild(docFrag);
});