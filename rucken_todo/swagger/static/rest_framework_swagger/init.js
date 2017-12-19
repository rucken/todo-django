$(function () {
  hljs.configure({
    highlightSizeThreshold: 5000
  });

  // Pre load translate...
  if(window.SwaggerTranslator) {
    window.SwaggerTranslator.translate();
  }
  var settings = {
    url: window.location.pathname + '?format=openapi',
    dom_id: "swagger-ui-container",
    onComplete: function(swaggerApi, swaggerUi){
      if(typeof initOAuth == "function") {
        initOAuth({
          clientId: "your-client-id",
          clientSecret: "your-client-secret-if-required",
          realm: "your-realms",
          appName: "your-app-name",
          scopeSeparator: ",",
          additionalQueryStringParams: {}
        });
      }

      if(window.SwaggerTranslator) {
        window.SwaggerTranslator.translate();
      }
      addApiKeyAuthorization();
    },
    onFailure: function(data) {
      log("Unable to Load SwaggerUI");
    },
  };
  $.extend(settings, JSON.parse($('#drs-settings').html()));

  window.swaggerUi = new SwaggerUi(settings);

  $('#input_apiKey').change(addApiKeyAuthorization);

  function addApiKeyAuthorization(){
    var key = encodeURIComponent($('#input_apiKey')[0].value);
    if(key && key.trim() != "") {
        var apiKeyAuth = new SwaggerClient.ApiKeyAuthorization("Authorization", "JWT " + key, "header");
        window.swaggerUi.api.clientAuthorizations.add("api_key", apiKeyAuth);
        log("added key " + key);
    }
  }

  window.swaggerUi.load();

  function log() {
    if ('console' in window) {
      console.log.apply(console, arguments);
    }
  }
});
