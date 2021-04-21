for (var i = 0; i < length; i++) {
  var element_result = document.getElementById('element1');
  (function(index){
    element_result.addEventListener("click", function() {
      console.log(index)
    })
  })(i)
  buttonsContainer.appendChild(element_result);

}
console.log(i);