

function openproduct(expid) {
    var myData
    $(document.body).on('click', "#exp1", function (e) {
        //doStuff
        console.log("hello")
        var exp_id = expid[0]
        $.ajax({
            type: "GET",
            url: "/singleProduct",
            data: exp_id,
            success: function (result) {
                myData = result
                console.log(myData)
                //alert(myData)
                if (myData != null || myData != "") {

                    console.log("hey");
                }

            }
        });
    });

}


