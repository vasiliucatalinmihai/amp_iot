
class Router:

    def __init__(self, router_config):
        self.routes = router_config

    def validate_request(self, request):
        if 'path' not in request.keys():
            raise Exception('Path missing')
        if 'data' not in request.keys():
            raise Exception('Data missing')
        if request['path'] not in self.routes.keys():
            raise Exception('Undefined route ' + request['path'])

    def get_controller(self, request):
        return self.routes[request['path']]['controller']

    def get_action(self, request):
        return self.routes[request['path']]['action'] + '_action'

    def get_params(self, request):
        return request['data']
