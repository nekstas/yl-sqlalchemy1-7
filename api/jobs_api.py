# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import datetime

import flask
from flask import jsonify, make_response, request

from data.db_session import create_session
from data.jobs import Jobs

ALL_KEYS = (
    'team_leader', 'job', 'work_size', 'collaborators',
    'start_date', 'end_date', 'is_finished'
)

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    session = create_session()
    jobs = session.query(Jobs).all()
    return jsonify({
        'jobs': [
            job.to_dict()
            for job in jobs
        ]
    })


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = create_session()
    job = session.query(Jobs).get(job_id)

    if not job:
        return make_response(jsonify({'error': 'Not Found'}), 404)

    return jsonify({
        'job': job.to_dict()
    })


@blueprint.route('/api/jobs/<path:any_>', methods=['GET', 'DELETE', 'PUT'])
def get_one_job_url_error(any_):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ALL_KEYS):
        return jsonify({'error': 'Bad request'})

    session = create_session()

    try:
        job = Jobs()
        job.team_leader = request.json['team_leader']
        job.job = request.json['job']
        job.work_size = request.json['work_size']
        job.collaborators = request.json['collaborators']
        if request.json['start_date'] is not None:
            job.start_date = datetime.datetime.fromisoformat(request.json['start_date'])
        if request.json['end_date'] is not None:
            job.end_date = datetime.datetime.fromisoformat(request.json['end_date'])
        job.is_finished = request.json['is_finished']

        session.add(job)
        session.commit()
    except Exception as e:
        _ = e
        return jsonify({'error': 'Invalid data'})

    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    session = create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not Found'}), 404)

    session.delete(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    session = create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not Found'}), 404)

    try:
        if 'team_leader' in request.json:
            job.team_leader = request.json['team_leader']
        if 'job' in request.json:
            job.job = request.json['job']
        if 'work_size' in request.json:
            job.work_size = request.json['work_size']
        if 'collaborators' in request.json:
            job.collaborators = request.json['collaborators']
        if 'start_date' in request.json:
            if request.json['start_date'] is None:
                job.start_date = None
            else:
                job.start_date = datetime.datetime.fromisoformat(request.json['start_date'])
        if 'end_date' in request.json:
            if request.json['end_date'] is None:
                job.end_date = None
            else:
                job.end_date = datetime.datetime.fromisoformat(request.json['end_date'])
        if 'is_finished' in request.json:
            job.is_finished = request.json['is_finished']

        session.merge(job)
        session.commit()
    except Exception as e:
        _ = e
        return jsonify({'error': 'Invalid data'})

    return jsonify({'success': 'OK'})
