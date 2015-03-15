'use strict';

angular.module('squirrel')
  .controller('NavbarCtrl', ["$scope", "$location", function($scope, $location) {
    $scope.date = new Date();

    $scope.navLinks = [
      {
        title: '',
        linktext: 'Home',
      }, {
        title: 'screeners',
        linktext: 'Screeners'
      }, {
        title: 'my-portfolios',
        linktext: 'My Portfolios'
      }, {
        title: 'doc',
        linktext: 'Documentation'
      }
    ];

    $scope.navClass = function(page) {
      console.log("location: " + $location.path());
      console.log("page: " + page);
      if ($location.path() === "/" && page === '') {
        console.log("returning active!")
        return "active";
      }
      var currentRoute = $location.path().substring(1) || '/';
      return page === currentRoute ? 'active' : '';
    };
  }]);
