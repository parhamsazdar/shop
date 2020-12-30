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

    function handleEditLink(product) {
        $(document.getElementById(product._id)).find('a[href="#Modal_edit"]').click(function () {
            $('#Modal_edit').prop('value', product._id)
        })
    }

    function setChange(product) {
        var $tds = $(document.getElementById(product._id)).find('td')
<<<<<<< HEAD
        $($tds[0]).prop('src', product.url_image)
=======
        $($tds[0]).find('img').attr('src', product.url_image)
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91
        $($tds[1]).html(product.name_product)
        $($tds[2]).html(product.category)
    }


    $.get('/api/product/list', function (resp) {
        console.log(resp)
        resp.forEach(product => createRow(product))
    })

    $('#Modal_add #button').click(function () {
        var form_data=new FormData($('#Modal_add #upload-file')[0])
        form_data.append("product_name",$('#Modal_add #product_name').val())
        form_data.append("category",$('#Modal_add #inputGroupSelect01').val())
        form_data.append("description",$('#Modal_add #description').val())
        $.ajax({
            url: '/api/product/add',
<<<<<<< HEAD
            data: {
                product_name: `${$('#Modal_add #product_name').val()}`,
                category: `${$('#Modal_add #inputGroupSelect01').val()}`,
                description: `${$('#Modal_add #description').val()}`
            },
=======
            data: form_data,
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91
            type: 'POST',
             contentType: false,
            cache: false,
            processData: false,
            success:
                function (resp) {
                    resp.forEach(product => createRow(product))
<<<<<<< HEAD
                    $('#Modal_edit').modal('hide')
=======
                    $('#Modal_add').modal('hide')
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91
                }
        })
    })


    $('#Modal_edit #button').click(function () {
<<<<<<< HEAD
        $.ajax({
            url: '/api/product/edit',
            data: {
                _id: $("#Modal_edit").prop('value'),
                product_name: `${$('#Modal_edit #product_name').val()}`,
                category: `${$('#Modal_edit #inputGroupSelect01').val()}`,
                description: `${$('#Modal_edit #description').val()}`
            },
=======
        var form_data=new FormData($('#Modal_edit #upload-file')[0])
        form_data.append("_id",$("#Modal_edit").prop('value'))
        form_data.append("product_name",$('#Modal_edit #product_name').val())
        form_data.append("category",$('#Modal_edit #inputGroupSelect01').val())
        form_data.append("description",$('#Modal_edit #description').val())
        $.ajax({
            url: '/api/product/edit',
            data: form_data,
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91
            type: 'POST',
             contentType: false,
            cache: false,
            processData: false,
            success:
                function (resp) {
                    resp.forEach(product => setChange(product))
                    $('#Modal_edit').modal('hide')
<<<<<<< HEAD
                }

        })
    })
    $('#upload-file-btn').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/api/product/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (resp) {
                if (!(resp[0].error)) {
                    resp.forEach(product => createRow(product))
                    $('#Modal_import').modal('hide')
                } else {
                    alert(resp[0].error)
                }

=======
                }
        })
    })
    $('#Modal_import #upload-file-btn').click(function () {
        var form_data_1 = new FormData($('#Modal_import #upload-file')[0]);
        form_data_1.append("_id","parham")
        $.ajax({
            type: 'POST',
            url: '/api/product/upload',
            data: form_data_1
            ,
            contentType: false,
            cache: false,
            processData: false,
            success: function (resp) {
                console.log(resp)
                if (!(resp[0].error)) {

                    resp.forEach(product => createRow(product))
                    $('#Modal_import').modal('hide')
                } else {
                    alert(resp[0].error)
                }

>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91
            },
        });
    });

})