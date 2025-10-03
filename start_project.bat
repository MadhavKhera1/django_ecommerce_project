@echo off
echo ========================================
echo    Starting Ecommerce Project
echo ========================================

REM Navigate to project directory
cd /d "C:\Users\91884\Desktop\KJC\ecomm"

REM Activate virtual environment
echo Activating virtual environment...
call .\env\Scripts\activate.bat

REM Install/update requirements (including Pillow)
echo Installing/updating requirements...
pip install -r requirements.txt

REM Set Python path
echo Setting Python path...
set PYTHONPATH=C:\Users\91884\Desktop\KJC\ecomm\ec

REM Run migrations
echo Running database migrations...
python manage.py migrate

REM Create sample data (optional)
echo Creating sample data...
python manage.py populate_products
python manage.py create_sample_customer

REM Start server
echo ========================================
echo    Starting Django Development Server
echo ========================================
echo.
echo Website: http://localhost:8000
echo Admin:   http://localhost:8000/admin/
echo.
echo Press CTRL+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause