var ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]

// function removephoto(fileupload) {
//     var labels = document.getElementsByTagName('LABEL');
//     for (let fl in labels) {
//         if (fl.htmlFor == fileupload.name) {
//             console.log(labels[i].innerHTML);
//             if (fl.innerHTML === "Change Photo") {
//                 fl.innerHTML = "Add a Picture";
//             }
//         }
//     }
// }
function uploadFile(fileUpload) {
    if (checkFileExt(fileUpload.value)) {
        var labels = document.getElementsByTagName('LABEL');
        for (let i = 0; i < labels.length; i++) {
            if (labels[i].htmlFor == fileUpload.name) {
                console.log(labels[i].innerHTML);
                labels[i].innerHTML = "Change Photo";
            }
        }
    }
    else {
        fileUpload.value = null;
    }
}

function checkFileExt(file) {
    let fileExtension;

    // Using regular expression.
    fileExtension = file.replace(/^.*\./, '');

    if (ALLOWED_EXTENSIONS.includes(fileExtension)) {
        return true;
    }
    return false;
}