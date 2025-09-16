# Ensure project root is on sys.path so 'apps' package can be imported in tests.
import sys
from pathlib import Path

root = Path(__file__).parent.resolve()
if str(root) not in sys.path:
    sys.path.insert(0, str(root))
