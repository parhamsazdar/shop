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
        deleteRow(product)
        handleEditLink(product)
    }
    function deleteRow(product) {
        res = $(document.getElementById(product._id)).find(".delete").click(function () {
            var $tr = $(this).closest('tr');
            url = '/api/product/delete/' + $tr.attr('id')
            $.get(url)
            $($tr).remove();

        })
    }

    function handleEditLink(product){
        $(document.getElementById(product._id)).find('a[href="#Modal_edit"]').click(function (){
            $('#Modal_edit').prop('value',product._id)
        })
    }

    function setChange(product){
        var $tds=$(document.getElementById(product._id)).find('td')
        $($tds[0]).prop('src',product.url_image)
        $($tds[1]).html(product.name_product)
        $($tds[2]).html(product.category)
    }


    $.get('/api/product/list', function (resp) {
        resp.forEach(product => createRow(product))
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
                    resp.forEach(product => createRow(product))
                    $('#Modal_edit').modal('hide')
                }
        })
    })


     $('#Modal_edit #button').click(function (){
          $.ajax({
            url: '/api/product/edit',
            data: {_id:$("#Modal_edit").prop('value'),
                product_name: `${$('#Modal_edit #product_name').val()}`,
                category: `${$('#Modal_edit #inputGroupSelect01').val()}`, description: `${$('#Modal_edit #description').val()}`
            },
            type: 'POST',
            success:
                function (resp) {
                    resp.forEach(product => setChange(product))
                    $('#Modal_edit').modal('hide')
                }

        })
    })
        $('#upload_button').click(function (){
            console.log(3)
            var fd = new FormData();
            var files = $('#file')[0].files;
            fd['file']=files[0]
            $.ajax({
                url:'/api/'



            })



    })

})