import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor

async def test_video_load(session, url, user_id):
    try:
        start_time = time.time()
        async with session.get(url) as response:
            if response.status == 200:
                # 模拟视频加载前几秒
                content = await response.read(1024 * 1024)  # 读取1MB
                load_time = time.time() - start_time
                return {"user": user_id, "status": "success", "load_time": load_time}
            else:
                return {"user": user_id, "status": "failed", "code": response.status}
    except Exception as e:
        return {"user": user_id, "status": "error", "error": str(e)}

async def run_load_test(base_url, concurrent_users):
    connector = aiohttp.TCPConnector(limit=concurrent_users)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(concurrent_users):
            task = test_video_load(session, base_url, i+1)
            tasks.append(task)
        
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time
        
        success_count = sum(1 for r in results if r["status"] == "success")
        avg_load_time = sum(r.get("load_time", 0) for r in results if r["status"] == "success") / max(success_count, 1)
        
        print(f"并发用户: {concurrent_users}")
        print(f"成功请求: {success_count}/{concurrent_users}")
        print(f"总耗时: {total_time:.2f}秒")
        print(f"平均加载时间: {avg_load_time:.2f}秒")
        print(f"成功率: {success_count/concurrent_users*100:.1f}%")

if __name__ == "__main__":
    # 测试不同并发级别
    base_url = "http://YOUR_EC2_IP:8080"  # 替换为你的EC2地址
    
    for users in [1, 5, 10, 20, 50]:
        print(f"\n=== 测试 {users} 并发用户 ===")
        asyncio.run(run_load_test(base_url, users))
        time.sleep(2)
