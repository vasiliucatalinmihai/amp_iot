

class AudioMap:

    def __init__(self):
        self._functions = self._get_functions()

    def getFunc(self, function_name):

        if function_name not in self._functions.keys():
            raise Exception('Function not found')

        return self._functions[function_name]

    @staticmethod
    def _get_functions():
        return {
            'setVolumesSoftStep': {
                'name': 'setVolumesSoftStep',
                'params': ()
            },
            'getVolumesSoftStep': {
                'name': 'getVolumesSoftStep',
                'params': ()
            },
            'getSpectrumData': {
                'name': 'getSpectrumData',
                'params': ()
            },
            'setMainVolume': {
                'name': 'setMainVolume',
                'params': ['value']
            },
            'getMainVolume': {
                'name': 'getMainVolume',
                'params': ()
            },
            'setLFSpeakerVolume': {
                'name': 'setLFSpeakerVolume',
                'params': ['value']
            },
            'getLFSpeakerVolume': {
                'name': 'getLFSpeakerVolume',
                'params': ()
            },
            'setRFSpeakerVolume': {
                'name': 'setRFSpeakerVolume',
                'params': ['value']
            },
            'getRFSpeakerVolume': {
                'name': 'getRFSpeakerVolume',
                'params': ()
            },
            'setLRSpeakerVolume': {
                'name': 'setLRSpeakerVolume',
                'params': ['value']
            },
            'getLRSpeakerVolume': {
                'name': 'getLRSpeakerVolume',
                'params': ()
            },
            'setRRSpeakerVolume': {
                'name': 'setRRSpeakerVolume',
                'params': ['value']
            },
            'getRRSpeakerVolume': {
                'name': 'getRRSpeakerVolume',
                'params': ()
            },
            'setSubVolume': {
                'name': 'setSubVolume',
                'params': ['value']
            },
            'getSubVolume': {
                'name': 'getSubVolume',
                'params': ()
            },
            'setMixGain': {
                'name': 'setMixGain',
                'params': ['value']
            },
            'getMixGain': {
                'name': 'getMixGain',
                'params': ()
            },
            'setMainSource': {
                'name': 'setMainSource',
                'params':  ['value']
            },
            'getMainSource': {
                'name': 'getMainSource',
                'params': ()
            },
            'setMainSourceGain': {
                'name': 'setMainSourceGain',
                'params':  ['value']
            },
            'getMainSourceGain': {
                'name': 'getMainSourceGain',
                'params': ()
            },
            'setSecondSource': {
                'name': 'setSecondSource',
                'params':  ['value']
            },
            'getSecondSource': {
                'name': 'getSecondSource',
                'params': ()
            },
            'setSecondSourceGain': {
                'name': 'setSecondSourceGain',
                'params':  ['value']
            },
            'getSecondSourceGain': {
                'name': 'getSecondSourceGain',
                'params': ()
            },
            'setSecondSourceRearSource': {
                'name': 'setSecondSourceRearSource',
                'params':  ['value']
            },
            'getSecondSourceRearSource': {
                'name': 'getSecondSourceRearSource',
                'params': ()
            },
            'setLoudness': {
                'name': 'setLoudness',
                'params':  ['value']
            },
            'getLoudness': {
                'name': 'getLoudness',
                'params': ()
            },
            'setLoudnessFreq': {
                'name': 'setLoudnessFreq',
                'params':  ['value']
            },
            'getLoudnessFreq': {
                'name': 'getLoudnessFreq',
                'params': ()
            },
            'setLoudnessBoost': {
                'name': 'setLoudnessBoost',
                'params':  ['value']
            },
            'getLoudnessBoost': {
                'name': 'getLoudnessBoost',
                'params': ()
            },
            'setLoudnessSoftStep': {
                'name': 'setLoudnessSoftStep',
                'params':  ['value']
            },
            'getLoudnessSoftStep': {
                'name': 'getLoudnessSoftStep',
                'params': ()
            },
            'setSoftMute': {
                'name': 'setSoftMute',
                'params':  ['value']
            },
            'getSoftMute': {
                'name': 'getSoftMute',
                'params': ()
            },
            'setSoftMuteEnable': {
                'name': 'setSoftMuteEnable',
                'params':  ['value']
            },
            'getSoftMuteEnable': {
                'name': 'getSoftMuteEnable',
                'params': ()
            },
            'setSoftMutePin': {
                'name': 'setSoftMutePin',
                'params':  ['value']
            },
            'getSoftMutePin': {
                'name': 'getSoftMutePin',
                'params': ()
            },
            'setSoftMuteTime': {
                'name': 'setSoftMuteTime',
                'params':  ['value']
            },
            'getSoftMuteTime': {
                'name': 'getSoftMuteTime',
                'params': ()
            },
            'setSoftMuteTimeStep': {
                'name': 'setSoftMuteTimeStep',
                'params':  ['value']
            },
            'getSoftMuteTimeStep': {
                'name': 'getSoftMuteTimeStep',
                'params': ()
            },
            'setTreble': {
                'name': 'setTreble',
                'params':  ['value']
            },
            'getTreble': {
                'name': 'getTreble',
                'params': ()
            },
            'setTrebleCenterFreq': {
                'name': 'setTrebleCenterFreq',
                'params':  ['value']
            },
            'getTrebleCenterFreq': {
                'name': 'getTrebleCenterFreq',
                'params': ()
            },
            'setTrebleReferenceOutput': {
                'name': 'setTrebleReferenceOutput',
                'params':  ['value']
            },
            'getTrebleReferenceOutput': {
                'name': 'getTrebleReferenceOutput',
                'params': ()
            },
            'setMiddle': {
                'name': 'setMiddle',
                'params':  ['value']
            },
            'getMiddle': {
                'name': 'getMiddle',
                'params': ()
            },
            'setMiddleQFactor': {
                'name': 'setMiddleQFactor',
                'params':  ['value']
            },
            'getMiddleQFactor': {
                'name': 'getMiddleQFactor',
                'params': ()
            },
            'setMiddleSoftStep': {
                'name': 'setMiddleSoftStep',
                'params':  ['value']
            },
            'getMiddleSoftStep': {
                'name': 'getMiddleSoftStep',
                'params': ()
            },
            'setBass': {
                'name': 'setBass',
                'params':  ['value']
            },
            'getBass': {
                'name': 'getBass',
                'params': ()
            },
            'setBassQFactor': {
                'name': 'setBassQFactor',
                'params':  ['value']
            },
            'getBassQFactor': {
                'name': 'getBassQFactor',
                'params': ()
            },
            'setBassSoftStep': {
                'name': 'setBassSoftStep',
                'params':  ['value']
            },
            'getBassSoftStep': {
                'name': 'getBassSoftStep',
                'params': ()
            },
            'setSubSetupCutFreq': {
                'name': 'setSubSetupCutFreq',
                'params':  ['value']
            },
            'getSubSetupCutFreq': {
                'name': 'getSubSetupCutFreq',
                'params': ()
            },
            'setSubSetupMiddleFreq': {
                'name': 'setSubSetupMiddleFreq',
                'params':  ['value']
            },
            'getSubSetupMiddleFreq': {
                'name': 'getSubSetupMiddleFreq',
                'params': ()
            },
            'setSubSetupBassFreq': {
                'name': 'setSubSetupBassFreq',
                'params':  ['value']
            },
            'getSubSetupBassFreq': {
                'name': 'getSubSetupBassFreq',
                'params': ()
            },
            'setSubSetupDcMode': {
                'name': 'setSubSetupDcMode',
                'params':  ['value']
            },
            'getSubSetupDcMode': {
                'name': 'getSubSetupDcMode',
                'params': ()
            },
            'setSubSetupSmooth': {
                'name': 'setSubSetupSmooth',
                'params':  ['value']
            },
            'getSubSetupSmooth': {
                'name': 'getSubSetupSmooth',
                'params': ()
            },
            'setMixLevel': {
                'name': 'setMixLevel',
                'params':  ['value']
            },
            'getMixLevel': {
                'name': 'getMixLevel',
                'params': ()
            },
            'setMixLevelLFS': {
                'name': 'setMixLevelLFS',
                'params':  ['value']
            },
            'getMixLevelLFS': {
                'name': 'getMixLevelLFS',
                'params': ()
            },
            'setMixLevelRFS': {
                'name': 'setMixLevelRFS',
                'params':  ['value']
            },
            'getMixLevelRFS': {
                'name': 'getMixLevelRFS',
                'params': ()
            },
            'setMixLevelEnable': {
                'name': 'setMixLevelEnable',
                'params':  ['value']
            },
            'getMixLevelEnable': {
                'name': 'getMixLevelEnable',
                'params': ()
            },
            'setMixLevelSubEnable': {
                'name': 'setMixLevelSubEnable',
                'params':  ['value']
            },
            'getMixLevelSubEnable': {
                'name': 'getMixLevelSubEnable',
                'params': ()
            },
            'setGainEffectForDso': {
                'name': 'setGainEffectForDso',
                'params': ['value']
            },
            'getGainEffectForDso': {
                'name': 'getGainEffectForDso',
                'params': ()
            },
            'setSpectrumQFactor': {
                'name': 'setSpectrumQFactor',
                'params': ['value']
            },
            'getSpectrumQFactor': {
                'name': 'getSpectrumQFactor',
                'params': ()
            },
            'setSpectrumSource': {
                'name': 'setSpectrumSource',
                'params': ['value']
            },
            'getSpectrumSource': {
                'name': 'getSpectrumSource',
                'params': ()
            },
            'setSpectrumRun': {
                'name': 'setSpectrumRun',
                'params': ['value']
            },
            'getSpectrumRun': {
                'name': 'getSpectrumRun',
                'params': ()
            },
            'setChipReset': {
                'name': 'setChipReset',
                'params': ['value']
            },
            'getChipReset': {
                'name': 'getChipReset',
                'params': ()
            },
            'setChipResetMode': {
                'name': 'setChipResetMode',
                'params': ['value']
            },
            'getChipResetMode': {
                'name': 'getChipResetMode',
                'params': ()
            },
            'setChipClockSource': {
                'name': 'setChipClockSource',
                'params': ['value']
            },
            'getChipClockSource': {
                'name': 'getChipClockSource',
                'params': ()
            },
            'setCouplingMode': {
                'name': 'setCouplingMode',
                'params': ['value']
            },
            'getCouplingMode': {
                'name': 'getCouplingMode',
                'params': ()
            },
            'setMute' : {
                'name': 'setMute',
                'params': ['mute']
            },
            'getMute': {
                'name': 'getMute',
                'params': ()
            },
            'setPower': {
                'name': 'setPower',
                'params': ['value']
            },
            'getPower': {
                'name': 'getPower',
                'params': ()
            },
            'setBits': {
                'name': 'setBits',
                'params': ('data', 'value', 'mask', 'pos')
            },
            'reset': {
                'name': 'reset',
                'params': ()
            },
            'resetToDefault': {
                'name': 'resetToDefault',
                'params': ()
            },
            'saveAll': {
                'name': 'saveAll',
                'params': ()
            },
        }
