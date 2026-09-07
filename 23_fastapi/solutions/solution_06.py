"""Solution 06 -- The document nobody wrote."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

spec = TestClient(app).get("/openapi.json").json()

print(len(spec["paths"]), "paths")

for path, methods in spec["paths"].items():
    if "post" in methods:
        print(path, "post")

limit_in = spec["components"]["schemas"]["LimitIn"]
print("LimitIn requires", limit_in["required"])

celsius = limit_in["properties"]["celsius"]
# gt and lt became exclusiveMinimum and exclusiveMaximum -- JSON Schema's names for
# the same two bounds. `ge` and `le` would have become minimum and maximum.
print(
    f"celsius exclusiveMinimum={celsius['exclusiveMinimum']}"
    f" exclusiveMaximum={celsius['exclusiveMaximum']}"
)

one = spec["paths"]["/summary/{location}"]["get"]
ref = one["responses"]["200"]["content"]["application/json"]["schema"]["$ref"]
print("/summary/{location} ->", ref.rsplit("/", 1)[-1])

# 422 is here because the path has a parameter that can fail to parse -- FastAPI
# added it. The 404 is not here, because a `raise` inside the function is not
# something an annotation can be read off.
print("documented statuses:", sorted(one["responses"]))
