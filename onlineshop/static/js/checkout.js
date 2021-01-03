$(document).ready(function () {
  params = new URLSearchParams(window.location.search);

  $("#record_form").submit(function (e) {
    var form = $(this);
    e.preventDefault(); // avoid to execute the actual submit of the form.
    for (let param of params) {
      var input =
        "<input  name='" +
        param[0] +
        "' style='display: none' value='" +
        param[1] +
        "'/>";
      form.append(input);
    }

    // form.append('parham','sazdar')

    var url = form.attr("action");

    $.ajax({
      type: "POST",
      url: url,
      data: form.serialize(), // serializes the form's elements.
      success: function (resp) {
        console.log(resp);
        alert("خرید شما ثبت شد");
        window.location.href = "/";
      }
    });
  });
});
