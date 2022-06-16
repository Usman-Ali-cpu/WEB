$(document).ready(function () {
    $('#table_id').DataTable();
});


// or!

$('#myTable').DataTable({
    columns: [
        { data: "tour_id" },
        { data: "tour_title" },
        { data: "tour_price_default" },
        { data: "tour_days" },
        { data: "tour_location" },
        { data: "tour_capacity" },
        { data: "tour_start_date" },
        { data: "tour_end_date" }
    ]
});


$('#myTable1').DataTable({
    columns: [
        { data: "experience_id" },
        { data: "experience_title" },
        { data: "experience_price_default" },
        { data: "experience_days" },
        { data: "experience_location" },
        { data: "experience_start_date" },
        { data: "experience_end_date" }
    ]
});