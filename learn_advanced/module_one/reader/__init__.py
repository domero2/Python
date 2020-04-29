from .compressed.gzipped import opener as gzip_opener
from .compressed.bzipped import opener as bz2_opener

__all__ = ['bz2_opener','gzip_opener']

print('reader is being imported')
