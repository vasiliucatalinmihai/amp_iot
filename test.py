# from amp_iot.src.amp.app import AmpApp
# #
# #
# # p = AmpApp.get_object_manager().get('amp_iot.src.amp.driver.preamp.Preamp')
# # server = Server(AmpApp, 'localhost', 7004, 0)
# # server.start()
# #
# data = {
#     'method_name': 'setMainVolume',
#     'args': {0: 4}
# }
#
# rd = {'path': 'mopidy/audio_option', 'data': data}
# AmpApp.run(rd)
#
# from amp_iot.src.lib.framework.client import Client
# c = Client('localhost', 7020)
# data = {
#     'method_name': 'getMainVolume',
#     'args': {}
# }
# c.send('mopidy/audio_option', data)


from amp_iot.src.amp.main import AmplifierMain

amp = AmplifierMain()

amp.run()

a=3

