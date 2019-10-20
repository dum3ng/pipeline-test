def _file_ext_name(url_like):
    splits = url_like.split('.')
    return splits[-1] if len(splits) > 1 else None


def _file_base_name(url_like):
    """
    return the last segment in a url without the extension.
    i.e  s3://some/path.ext will return `path`
    """
    ext_name = _file_ext_name(url_like)
    if ext_name:
        return url_like.split('/')[-1][0:-(len(ext_name)+1)]
    else:
        return url_like.split('/')[-1]


a = 's3://some/path.ext'

ext = _file_ext_name(a)
print(ext)

base = _file_base_name(a)
print(base)
