from flask import Blueprint, render_template, request
from .models import Event

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    events = Event.query.all()
    return render_template('event_list.html', events=events)

@main_routes.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        # handle form submission
        pass
    return render_template('create_event.html')
