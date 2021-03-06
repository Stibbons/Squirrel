'use strict';

angular.module('squirrel').factory('debug',

  ["$log",

    function($log) {

      this.debug_settings = [];
      var debug_service = {
        enabled: true,
      };
      debug_service.disable = function() {
        debug_service.enabled = false;
      }

      debug_service.log = function(module, text) {
        if (debug_service.enabled) {
          $log.log("LOG: [" + module + "] " + text);
        }
      };

      debug_service.warn = function(module, text) {
        $log.warn("WARN: %c [" + module + "] " + text,
          'background: #CF8902; color: #000000');
      };

      debug_service.info = function(module, text) {
        if (debug_service.enabled) {
          $log.info("INFO: %c [" + module + "] " + text,
            'color: #0006FF');
        }
      };

      debug_service.error = function(module, text) {
        $log.error("ERROR: %c [" + module + "] " + text,
          'background: #E20000; color: #FFFFFF');
      };

      debug_service.debug = function(module, text) {
        if (debug_service.enabled) {
          $log.debug("DEBUG: %c [" + module + "] " + text, 'background: #FFFFFF; color: #444444');
        }
      };

      debug_service.dump = function(module, obj, name) {
        if (debug_service.enabled) {
          if (!name) {
            name = "Object"
          }
          $log.log("LOG: %c [" + module + "] " + name + ": " + JSON.stringify(obj),
            'background: #DFDFDF; color: #000000#000000');
        }
      };

      return debug_service;
    }
  ]
);
