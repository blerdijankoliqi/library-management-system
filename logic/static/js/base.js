/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
ind = 1
function openNav() {
    if (ind == 1) {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.getElementById("openbtn").style.display = "none";
        ind= 0
    } else{
        document.getElementById("mySidebar").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
        document.getElementById("openbtn").style.display = "block";
        ind=1
    }
  }
  
//   /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
//   function closeNav() {
//     if (ind == 0){
//     document.getElementById("mySidebar").style.width = "0";
//     document.getElementById("main").style.marginLeft = "0";
//     ind=1
// }
//   }