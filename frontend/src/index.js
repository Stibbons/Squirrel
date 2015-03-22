var app;

app = angular.module("squirrel", ['ngAnimate', 'ngCookies',
  'ngTouch', 'ngSanitize',
  'ngResource', 'ngRoute',
  'ui.bootstrap'
]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "app/homepage/homepage.template.html",
      controller: "HomepageCtrl",
      /*      resolve: {
              auth: ["$q", "AuthenticationService", function($q, AuthenticationService) {
                var userInfo = AuthenticationService.getUserInfo();

                if (userInfo) {
                  return $q.when(userInfo);
                } else {
                  return $q.reject({
                    authenticated: false
                  });
                }
              }]
            }*/
    })
    .when("/my-portfolios", {
      templateUrl: "app/my-portfolios/my-portfolios.template.html",
      controller: "MyPortfoliosCtrl"
    })
    .when("/screeners", {
      templateUrl: "app/screeners/screeners.template.html",
      controller: "ScreenersCtrl"
    })
    .when("/login", {
      templateUrl: "app/login/login.template.html",
      controller: "LoginCtrl"
    })
    .when("/register", {
      templateUrl: "app/register/register.template.html",
      controller: "RegisterCtrl"
    })
    .when("/settings", {
      templateUrl: "app/settings/settings.template.html",
      controller: "SettingsCtrl"
    })
    .when("/doc", {
      controller: function() {
        window.location.replace('/doc');
      },
      template: "<div></div>"
    })
    .otherwise({
      redirectTo: "/"
    });

  $locationProvider.html5Mode({
    enabled: false,
  });
}]);
