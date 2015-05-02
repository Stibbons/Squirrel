'use strict';

angular.module("squirrel").controller("PortfolioOverviewCreateController",

  ["$scope", "$location", "gettextCatalog", "Restangular", "LocationWatcherService", "request",
  "$sce",

    function($scope, $location, gettextCatalog, Restangular, LocationWatcherService, request,
      $sce) {

      $scope.portfolioTypes = {};
      $scope.currentType = null;
      $location.search("a", "create");

      $scope.refresh = function() {
        console.log("currentType = " + JSON.stringify($scope.currentType));
        if ($scope.currentType) {
          _.forEach($scope.types, function(item) {
            console.log("item = " + JSON.stringify(item));
            console.log("item.name = " + JSON.stringify(item.name));
            if (item.name == $scope.currentType) {
              $scope.portfolioTypes = {
                selected: item
              };
            }
          });
        }
      };

      $scope.getPortfolioTypes = function() {
        request.request("api/portfolios/types").then(function(data) {
          console.log("received portfolios types: " + JSON.stringify(data));
          $scope.portfolioTypes = data;
          $scope.refresh();
          $scope.createPortfolio.$setPristine();
          $scope.createPortfolio.portfolioType.$setPristine();
        });
      };
      $scope.getPortfolioTypes();

      $scope.groupPerAccountTypes = function(item) {
        return item[0];
      };
      /*
      $scope.setupWatchers = function($scope, scopeVarName, nameKey) {
        $scope.$watch(function() {
          return $location.search();
        }, function() {
          $scope[scopeVarName] = $location.search()[nameKey] || "";
        });
        $scope.$watch(scopeVarName, function(portfolioName) {
          $location.search(nameKey, portfolioName);
        });
      };
      */
      LocationWatcherService.setupWatchers($scope, "portfolioName", "n");
      LocationWatcherService.setupWatchers($scope, "portfolioDescription", "d");
      LocationWatcherService.setupWatchers($scope, "portfolioTypes.selected.name", "t");
    }
  ]
);