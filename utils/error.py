class VideoCodecError(Exception):
    """When the video fails to re-encode/unsupported file format"""
    pass

class MinThreadError(Exception):
    """When the threads selected is 0"""
    pass

class MaxThreadError(Exception):
    """When the threads are more or equal to 24"""
    pass

class LoadingSettingsError(Exception):
    """When for whatever reason settings cant be loaded"""
    pass

class DirectoryError(Exception):
    pass

class CodecError(Exception):
    pass