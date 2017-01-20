//Javascript function to set the active page to class active in the navbar

function setActive() {
  aObj = document.getElementById('nav-menu').getElementsByTagName('a');
  for(i=0;i<aObj.length;i++) { 
    if(document.location.href.indexOf(aObj[i].href)>=0) {
      aObj[i].parentElement.className+=' active';
    }
  }
}

window.onload = setActive;