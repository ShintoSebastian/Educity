document.getElementById('default').click();
function swap(ele) {
    var i;
    var x=document.getElementsByClassName("content");
    
    for(i=0;i<x.length;i++){
        x[i].style.display="none"
      
    }
    document.getElementById(ele).style.display="block";    
}
