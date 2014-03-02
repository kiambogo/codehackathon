var app = angular.module("myApp", ['elasticsearch']);
app.service('es', function (esFactory) {
  return esFactory({
  	"host": "taxr.ca:9200"
  });
});

app.controller("SearchController", ["$window", "$scope", "es", function($window, $scope, es) {
	$scope.foo = 'bar';

	$scope.doSomething = function(response) {
		es.search({
			index: 'data',
			type: 'MinistryData',
			limit: 5
		})
	};
}]);