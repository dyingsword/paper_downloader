import requests

#列出所需 DBLP 的作者搜索和文献搜索 API 地址
DBLP_AUTHOR_API = "https://dblp.org/search/author/api"
DBLP_PUB_API    = "https://dblp.org/search/publ/api"

# 自定义的请求头，模拟浏览器访问
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; DBLPScraper/1.0; +https://dblp.org/)"
    )
}

def get_author_pid(name: str, time_out: float = 10.0) -> str:
    """
    根据作者姓名，在 DBLP 上搜索并返回该作者的 PID（如 "09/2187"）。
    """
    params = {
        "q": name,
        "format": "json",
        "h": 5  # 最多返回 5 条候选
    }
    resp = requests.get(DBLP_AUTHOR_API,
                        params=params,
                        headers=HEADERS,
                        timeout=time_out)
    resp.raise_for_status()
    data = resp.json()

    # 从 hits 列表中取第一个结果
    hits = data.get("result", {}) \
               .get("hits", {}) \
               .get("hit", [])
    if not hits:
        raise ValueError(f"未找到作者：{name}")
    top_info = hits[0].get("info", {})

    pid_url = top_info.get("url")
    if not pid_url or not pid_url.startswith("https://dblp.org/pid/"):
        raise ValueError("未找到有效的 PID URL")

    pid = pid_url.split("https://dblp.org/pid/")[-1]
    return pid
print(get_author_pid("Ya-qin Zhang"))