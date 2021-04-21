function LoopTest() {
    var i=0;
    var stop=5;
    for (i=0;i<5;i++) {  
     var v = document.createElement('input');
     v.type="button";
     v.value="Button " +i;
     document.getElementById('test').appendChild(v);
    }
    }