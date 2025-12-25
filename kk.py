def create_blessing_html():
    html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>满屏祝福效果</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            min-height: 100vh;
            overflow: hidden;
            font-family: 'Microsoft YaHei', sans-serif;
        }

        .container {
            position: relative;
            width: 100%;
            height: 100vh;
        }

        .blessing {
            position: absolute;
            padding: 15px 25px;
            background: linear-gradient(45deg, #ff6b6b, #ffa726, #ffee58, #4cd964, #5ac8fa, #007aff, #5856d6);
            background-size: 400% 400%;
            color: white;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            cursor: pointer;
            white-space: nowrap;
            opacity: 0;
            animation: gradient 3s ease infinite;
            z-index: 1000;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .controls {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 2000;
            background: rgba(255,255,255,0.9);
            padding: 15px 25px;
            border-radius: 50px;
            display: flex;
            gap: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .title {
            text-align: center;
            color: white;
            font-size: 48px;
            margin-top: 100px;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px #fff; }
            to { text-shadow: 0 0 20px #fff, 0 0 30px #ff0066; }
        }
    </style>
</head>
<body>
    <h1 class="title">🎉 满屏祝福 🎊</h1>

    <div class="controls">
        <button id="startBtn">开始祝福</button>
        <button id="stopBtn">暂停祝福</button>
        <button id="clearBtn">清空祝福</button>
        <button id="fireworksBtn">烟花模式</button>
    </div>

    <div class="container" id="container"></div>

    <script>
        const blessings = [
            "🎉 恭喜发财！", "❤️ 心想事成！", "✨ 万事如意！", 
            "🎊 新年快乐！", "🌟 吉祥如意！", "🍀 一帆风顺！",
            "💝 阖家幸福！", "🎁 大吉大利！", "🎈 步步高升！",
            "🏮 福星高照！", "💖 身体健康！", "🎯 事业有成！",
            "🌈 好运连连！", "🎨 创意无限！", "💰 财源广进！",
            "🍎 平平安安！", "🌺 花开富贵！", "🥂 阖家欢乐！",
            "🎇 前程似锦！", "🎆 喜气洋洋！", "🌸 春满人间！",
            "🦋 梦想成真！", "🎶 笑口常开！", "🪅 天天开心！"
        ];

        const emojis = ["🎉", "❤️", "✨", "🎊", "🌟", "🍀", "💝", "🎁", "🎈", "🏮", "💖", "🎯"];

        let isActive = false;
        let intervalId = null;
        let isFireworksMode = false;

        const container = document.getElementById('container');

        // 创建祝福元素
        function createBlessing() {
            const blessing = document.createElement('div');
            blessing.className = 'blessing';

            // 随机选择祝福语
            const text = blessings[Math.floor(Math.random() * blessings.length)];
            const emoji = emojis[Math.floor(Math.random() * emojis.length)];

            // 随机位置（考虑边界）
            const maxX = window.innerWidth - 200;
            const maxY = window.innerHeight - 100;
            const x = Math.random() * maxX;
            const y = Math.random() * maxY;

            blessing.textContent = isFireworksMode ? emoji + ' ' + text : text;
            blessing.style.left = `${x}px`;
            blessing.style.top = `${y}px`;

            // 随机大小
            const size = Math.random() * 0.5 + 0.8;
            blessing.style.fontSize = `${24 * size}px`;
            blessing.style.transform = `scale(${size})`;

            // 随机颜色（如果不是烟花模式）
            if (!isFireworksMode) {
                const hue = Math.random() * 360;
                blessing.style.background = `linear-gradient(45deg, 
                    hsl(${hue}, 100%, 60%), 
                    hsl(${(hue + 60) % 360}, 100%, 60%))`;
            }

            // 随机动画延迟
            const delay = Math.random() * 0.5;
            blessing.style.animationDelay = `${delay}s`;

            // 添加动画
            blessing.style.animation = `gradient 3s ease infinite, 
                ${getRandomAnimation()} 1.5s ease-out forwards`;

            container.appendChild(blessing);

            // 点击祝福语消失
            blessing.addEventListener('click', function() {
                this.style.animation = 'disappear 0.5s forwards';
                setTimeout(() => this.remove(), 500);
            });

            // 自动消失
            setTimeout(() => {
                if (blessing.parentNode) {
                    blessing.style.animation = 'disappear 0.5s forwards';
                    setTimeout(() => blessing.remove(), 500);
                }
            }, 3000);
        }

        // 获取随机动画效果
        function getRandomAnimation() {
            const animations = [
                'popIn', 'slideIn', 'bounceIn', 'fadeIn', 'zoomIn', 'rotateIn'
            ];

            return animations[Math.floor(Math.random() * animations.length)];
        }

        // 定义动画
        function defineAnimations() {
            const style = document.createElement('style');

            style.textContent = `
                @keyframes popIn {
                    0% { transform: scale(0); opacity: 0; }
                    70% { transform: scale(1.1); opacity: 1; }
                    100% { transform: scale(1); opacity: 1; }
                }

                @keyframes slideIn {
                    0% { transform: translateY(-100px) scale(0.5); opacity: 0; }
                    100% { transform: translateY(0) scale(1); opacity: 1; }
                }

                @keyframes bounceIn {
                    0% { transform: scale(0.3); opacity: 0; }
                    50% { transform: scale(1.05); opacity: 1; }
                    70% { transform: scale(0.9); }
                    100% { transform: scale(1); opacity: 1; }
                }

                @keyframes fadeIn {
                    0% { opacity: 0; transform: translateY(20px); }
                    100% { opacity: 1; transform: translateY(0); }
                }

                @keyframes zoomIn {
                    0% { transform: scale(0.5) rotate(-10deg); opacity: 0; }
                    100% { transform: scale(1) rotate(0); opacity: 1; }
                }

                @keyframes rotateIn {
                    0% { transform: scale(0) rotate(-180deg); opacity: 0; }
                    100% { transform: scale(1) rotate(0); opacity: 1; }
                }

                @keyframes disappear {
                    0% { transform: scale(1); opacity: 1; }
                    100% { transform: scale(0.5); opacity: 0; }
                }
            `;

            document.head.appendChild(style);
        }

        // 开始弹出祝福
        function startBlessings() {
            if (isActive) return;
            isActive = true;

            // 先清除现有祝福
            clearBlessings();

            // 立即创建几个祝福
            for (let i = 0; i < 5; i++) {
                setTimeout(() => createBlessing(), i * 200);
            }

            // 设置定时器持续创建
            intervalId = setInterval(() => {
                if (Math.random() > 0.3) { // 70%概率创建新祝福
                    createBlessing();
                }
            }, 500);
        }

        // 暂停祝福
        function stopBlessings() {
            isActive = false;
            clearInterval(intervalId);
        }

        // 清空所有祝福
        function clearBlessings() {
            const blessings = document.querySelectorAll('.blessing');
            blessings.forEach(blessing => {
                blessing.style.animation = 'disappear 0.5s forwards';
                setTimeout(() => blessing.remove(), 500);
            });
        }

        // 切换烟花模式
        function toggleFireworksMode() {
            isFireworksMode = !isFireworksMode;
            const btn = document.getElementById('fireworksBtn');
            btn.textContent = isFireworksMode ? '普通模式' : '烟花模式';
            btn.style.background = isFireworksMode ? 
                'linear-gradient(45deg, #ff0080, #ff8c00)' : 
                'linear-gradient(45deg, #6a11cb, #2575fc)';
        }

        // 按钮事件绑定
        document.getElementById('startBtn').addEventListener('click', startBlessings);
        document.getElementById('stopBtn').addEventListener('click', stopBlessings);
        document.getElementById('clearBtn').addEventListener('click', clearBlessings);
        document.getElementById('fireworksBtn').addEventListener('click', toggleFireworksMode);

        // 键盘快捷键
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case ' ':
                    isActive ? stopBlessings() : startBlessings();
                    break;
                case 'c':
                case 'C':
                    clearBlessings();
                    break;
                case 'f':
                case 'F':
                    toggleFireworksMode();
                    break;
            }
        });

        // 鼠标右键也可以创建祝福
        document.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            if (!isActive) return;

            const blessing = document.createElement('div');
            blessing.className = 'blessing';
            blessing.textContent = blessings[Math.floor(Math.random() * blessings.length)];
            blessing.style.left = `${e.clientX}px`;
            blessing.style.top = `${e.clientY}px`;
            blessing.style.animation = 'popIn 0.5s forwards, gradient 3s ease infinite';

            container.appendChild(blessing);

            setTimeout(() => {
                if (blessing.parentNode) {
                    blessing.style.animation = 'disappear 0.5s forwards';
                    setTimeout(() => blessing.remove(), 500);
                }
            }, 2000);
        });

        // 初始化动画定义
        defineAnimations();

        // 页面加载时自动开始（可选）
        window.addEventListener('load', () => {
            setTimeout(startBlessings, 1000);
        });

        // 窗口大小变化时调整
        window.addEventListener('resize', () => {
            if (isActive) {
                clearBlessings();
                setTimeout(() => {
                    for (let i = 0; i < 3; i++) {
                        setTimeout(() => createBlessing(), i * 200);
                    }
                }, 100);
            }
        });
    </script>
</body>
</html>'''

    return html_content


def save_html_file(filename="index.html"):
    """保存HTML文件到本地"""
    html_content = create_blessing_html()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML文件已保存为: {filename}")
    print("请用浏览器打开此文件查看效果")
    return filename


def open_in_browser(filename="index.html"):
    """在浏览器中打开HTML文件"""
    import webbrowser
    import os

    # 获取文件的绝对路径
    file_path = os.path.abspath(filename)

    # 用默认浏览器打开
    webbrowser.open(f'file://{file_path}')
    print("正在浏览器中打开...")
    return True


def create_and_open_blessings():
    """创建并打开祝福效果"""
    filename = save_html_file()
    open_in_browser(filename)
    return filename


# 主程序
if __name__ == "__main__":
    print("正在创建满屏祝福效果...")
    print("=" * 50)

    # 创建HTML文件
    filename = save_html_file()

    # 询问是否在浏览器中打开
    response = input("是否在浏览器中打开文件？(y/n): ").lower()
    if response in ['y', 'yes', '是', '1']:
        open_in_browser(filename)

    print("\n使用说明:")
    print("1. 点击'开始祝福'按钮开始弹出祝福")
    print("2. 点击'暂停祝福'按钮暂停")
    print("3. 点击'清空祝福'按钮清除所有祝福")
    print("4. 点击'烟花模式'切换显示样式")
    print("5. 点击祝福文字可以使其消失")
    print("6. 右键点击可以手动添加祝福")
    print("\n快捷键:")
    print("  空格键: 开始/暂停")
    print("  C键: 清空祝福")
    print("  F键: 切换烟花模式")