var reviewprofession = [];
var reviewdesc = [];
var total_len = document.getElementById('rev-len').getAttribute('name');
console.log(total_len);
for (var i = 0; i < total_len; i++) {
    console.log("reviews" + i + ".profession");
    var tm1 = document.getElementById("reviews" + i + ".profession").getAttribute("name");
    var tm2 = document.getElementById("reviews" + i + ".description").getAttribute("name");
    reviewprofession.push(tm1);
    reviewdesc.push(tm2);
    //Do what you need to do with tm1 and tm2. 
    console.log(tm1);
    console.log(tm2);
}
function changereview() {
    var rand1 = Math.floor(Math.random() * total_len);
    var rand2 = Math.floor(Math.random() * total_len);
    var rand3 = Math.floor(Math.random() * total_len);
    while (rand1 === rand2) {
        rand2 = Math.floor(Math.random() * total_len);
    }
    while (rand3 === rand1) {
        rand3 = Math.floor(Math.random() * total_len);
    }
    var prof1 = document.getElementById("profession");
    var des1 = document.getElementById("description");
    prof1.innerText = reviewprofession[rand1];
    des1.innerHTML = reviewdesc[rand1];

    var prof2 = document.getElementById("profession2");
    var des2 = document.getElementById("description2");
    prof2.innerText = reviewprofession[rand2];
    des2.innerHTML = reviewdesc[rand2];

    var prof3 = document.getElementById("profession3");
    var des3 = document.getElementById("description3");
    prof3.innerText = reviewprofession[rand3];
    des3.innerHTML = reviewdesc[rand3];
}