$(document).ready(function () {
  if (_.str.startsWith(window.location.pathname, "/shop/payment")) {
    // Hide Cash On Delivery payment acquirer from list
    var $payment_methods_inputs = $("input[name='pm_id']");
    var $cod_acquirer = $payment_methods_inputs.filter("[data-provider='cod']");
    $cod_acquirer.parent().parent().addClass("o_hidden");
    $cod_acquirer.prop("checked", false);

    // Prepare data for comparison and add  on click listener
    if (_.str.startsWith(window.location.pathname, "/shop/payment")) {
      $(".o_delivery_carrier_select").click(function (ev) {
        var carrier_name = $(this).find("*label").text();
        var provider_cod_name = $cod_acquirer
          .parent()
          .find(".payment_option_name")
          .text();
        // Remove spaces from names
        provider_cod_name = provider_cod_name.replace(/\s+/g, "");
        carrier_name = carrier_name.replace(/\s+/g, "");
        var $payment_method_acquirers = $("#payment_method .card");
        //console.log(carrier_name)
        //console.log(provider_cod_name)
        // Check if shipping method is COD if so hide payment methods and select COD provider
        if (provider_cod_name == carrier_name) {
          $payment_method_acquirers.addClass("o_hidden");
          $cod_acquirer.prop("checked", true);
        } else {
          $payment_method_acquirers.removeClass("o_hidden");
          $cod_acquirer.prop("checked", false);
        }
      });
    }
  }
});
