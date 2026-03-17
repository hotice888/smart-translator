@echo off
echo ========================================
echo Smart Translator - GitHub 发布指南
echo ========================================
echo.
echo 由于网络限制或仓库未创建，请按以下步骤操作：
echo.
echo 步骤 1: 在 GitHub 上创建仓库
echo ----------------------------------------
echo 1. 打开浏览器访问：https://github.com/new
echo 2. Repository name: smart-translator
echo 3. Description: AI-powered smart translator with batch processing
echo 4. 选择 Public
echo 5. 不要勾选 "Initialize this repository with a README"
echo 6. 点击 "Create repository"
echo.
echo 步骤 2: 推送代码到 GitHub
echo ----------------------------------------
echo 复制以下命令在命令行执行：
echo.
echo cd C:\Users\Administrator\.copaw\active_skills\smart-translator
echo git remote set-url origin https://github.com/hotice888/smart-translator.git
echo git push -u origin main
echo.
echo 或者使用 HTTPS 推送（需要输入 GitHub 用户名和 Token）：
echo git push -u origin main
echo.
echo 步骤 3: 验证发布成功
echo ----------------------------------------
echo 访问：https://github.com/hotice888/smart-translator
echo 确认代码已上传成功
echo.
echo 步骤 4: 安装技能
echo ----------------------------------------
echo clawdhub install hotice888/smart-translator
echo.
echo ========================================
echo 如需帮助，请查看 PUBLISH.md 文件
echo ========================================
pause
