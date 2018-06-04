import ssl

# 用非认证上下文替代认证上下文
ssl._create_default_https_context = ssl._create_unverified_context()