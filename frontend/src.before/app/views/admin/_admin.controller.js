'use strict';

// take ideas from:
// http://startbootstrap.com/template-overviews/sb-admin/
// http://ironsummitmedia.github.io/startbootstrap-sb-admin/index.html
angular.module('squirrel').controller('AdminCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS", "$location",
  "gettextCatalog",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS, $location,
      gettextCatalog) {

      $scope.is_admin = AuthenticationService.isAdmin();
      $scope.endpoint = "/admin";

      $scope.menuItems = [
        {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/admin/admin.dashboard.template.html'
        }, {
          'search': {
            "p": "crawlers"
          },
          'name': gettextCatalog.getString('Crawlers'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/admin/admin.crawlers.template.html'
        }
      ];
      $scope.currentPage = function(page) {
        var s = $location.search();
        if (_.isEmpty(s['p'])) {
          return "dashboard";
        }
        return s['p'];
      };

      $scope.activeIfCurrentPageIs = function(page) {
        var s = $location.search();
        var current_page;
        if (_.isEmpty(s['p'])) {
          current_page = "dashboard";
        } else {
          current_page = s['p'];
        }
        console.log("activeIfCurrentPageIs");
        console.log("current_page = " + JSON.stringify(current_page));
        console.log("page = " + JSON.stringify(page));
        if (current_page == page) {
          return "active";
        }
        return "";
      };

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("admin on loginSuccesful1:" + userName);
        $scope.is_admin = AuthenticationService.isAdmin();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("admin on logout");
        $scope.is_admin = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("admin on loginError:" + error);
        $scope.is_admin = false;
      });

    }
  ]
);
