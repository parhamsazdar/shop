$(document).ready(function () {
    $tbody = $("#product_table")

    function createRow(product) {
        var name = product.name_product;
        var category = product.category;
        var image = "<img src='" + product.url_image + "' style='width: 100px' >";
        var row = "<tr id='" + product._id + "'>";
        row += "<td>" + image + "</td>";
        row += "<td>" + name + "</td>";
        row += "<td>" + category + "</td>";
        row += "<td class='text-center'>" + "<a data-toggle=\"modal\" href=\"#Modal_edit\">ویرایش</a>" + "  " + "<a  class='delete' href=\"#\">حذف</a>" + "</td>";
        row += "</tr>";
        $tbody.append(row);
    }
    function deleteRow(product) {

        res = $(document.getElementById(product._id)).find(".delete").click(function () {
            var $tr = $(this).closest('tr');
            url = '/api/product/delete/' + $tr.attr('id')
            $.get(url)
            $($tr).remove();

        })
    }

    $.get('/api/product/list', function (resp) {
        var $resp = resp
        $resp.forEach(product => createRow(product))
        $resp.forEach(product => deleteRow(product))

    })

    $('#Modal_add #button').click(function () {
        $.ajax({
            url: '/api/product/add',
            data: {
                product_name: `${$('#Modal_add #product_name').val()}`,
                category: `${$('#Modal_add #inputGroupSelect01').val()}`, description: `${$('#Modal_add #description').val()}`
            },
            type: 'POST',
            success:
                function (resp) {
                    var $resp = resp
                    $resp.forEach(product => createRow(product))
                    $resp.forEach(product => deleteRow(product))
                }
        })
    })


     $('#Modal_edit #button').click(function (){
          $.ajax({
            url: '/api/product/edit',
            data: {
                product_name: `${$('#Modal_edit #product_name').val()}`,
                category: `${$('#Modal_edit #inputGroupSelect01').val()}`, description: `${$('#Modal_edit #description').val()}`
            },
            type: 'POST',
            success:
                function (resp) {
                    var $resp = resp
                    $resp.forEach(product => createRow(product))
                    $resp.forEach(product => deleteRow(product))
                }



     })





})

})