'use strict';

angular.module("squirrel").controller("PlansCtrl",

  ["$scope", "$location", "AuthenticationService", "$document",

    function($scope, $location, AuthenticationService, $document) {

      $document.scrollTo(0, 0);

    }
  ]
);
