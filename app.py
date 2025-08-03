from flask import Flask, jsonify, render_template
from metrics_collector import get_metrics
from alert_manager import load_thresholds, check_alerts

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    metrics = get_metrics()
    thresholds = load_thresholds()
    alerts = check_alerts(metrics, thresholds)
    return render_template('dashboard.html', metrics=metrics, alerts=alerts)

@app.route('/')
def home():
    metrics = get_metrics()
    thresholds = load_thresholds()
    alerts = check_alerts(metrics, thresholds)
    return jsonify({
        "metrics": metrics,
        "alerts": alerts
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
