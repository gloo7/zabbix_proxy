from task.const import D


rewriter_mapping = {k.rstrip('_rewriter'): globals(
)[k] for k in globals() if k.endswith('_rewriter')}
