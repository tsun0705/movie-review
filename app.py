from flask import Flask, render_template, jsonify, request, session, flash
from datetime import timedelta

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/index')
def getIndex():
    return render_template('index.html')


@app.route('/main')
def getMain():
    return render_template('main.html')

@app.route('/romence_one')
def romance_one():
    return render_template('romence_one.html')

@app.route('/romence_two')
def romance_two():
    return render_template('romence_two.html')

@app.route('/romence_three')
def romance_three():
    return render_template('romence_three.html')

@app.route('/romence_four')
def romance_four():
    return render_template('romence_four.html')

@app.route('/romence_five')
def romance_five():
    return render_template('romence_five.html')

@app.route('/action_one')
def action_one():
    return render_template('action_one.html')

@app.route('/action_two')
def action_two():
    return render_template('action_two.html')

@app.route('/action_three')
def action_three():
    return render_template('action_three.html')

@app.route('/action_four')
def action_four():
    return render_template('action_four.html')

@app.route('/action_five')
def action_five():
    return render_template('action_five.html')

@app.route('/comedy_one')
def comedy_one():
    return render_template('comedy_one.html')

@app.route('/comedy_two')
def comedy_two():
    return render_template('comedy_two.html')

@app.route('/comedy_three')
def comedy_three():
    return render_template('comedy_three.html')

@app.route('/comedy_four')
def comedy_four():
    return render_template('comedy_four.html')

@app.route('/comedy_five')
def comedy_five():
    return render_template('comedy_five.html')

@app.route('/ani_one')
def ani_one():
    return render_template('ani_one.html')

@app.route('/ani_two')
def ani_two():
    return render_template('ani_two.html')

@app.route('/ani_three')
def ani_three():
    return render_template('ani_three.html')

@app.route('/ani_four')
def ani_four():
    return render_template('ani_four.html')

@app.route('/ani_five')
def ani_five():
    return render_template('ani_five.html')

@app.route('/thriller_one')
def thriller_one():
    return render_template('thriller_one.html')

@app.route('/thriller_two')
def thriller_two():
    return render_template('thriller_two.html')

@app.route('/thriller_three')
def thriller_three():
    return render_template('thriller_three.html')

@app.route('/thriller_four')
def thriller_four():
    return render_template('thriller_four.html')

@app.route('/thriller_five')
def thriller_five():
    return render_template('thriller_five.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/post_movie', methods=['GET'])
def post_movie():
    reviews = list(db.hansson_review.find({},{'_id':False}))
    return jsonify({'all_reviews': reviews})

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    id_receive = request.form.get('id_give', False)
    pw_receive = request.form.get('pw_give', False)
    myName_receive = request.form.get('myName_give', False)
    dob_receive = request.form.get('dob_give', False)
    gender_receive = request.form.get('gender_give', False)
    phone_receive = request.form.get('phone_give', False)

    doc = {
        'id': id_receive,
        'pw': pw_receive,
        'myName': myName_receive,
        'dob': dob_receive,
        'gender': gender_receive,
        'phone': phone_receive
    }

    db.member.insert_one(doc)

    return jsonify({'msg': '회원가입 완료!'})

@app.route('/login', methods=['GET'])
def read_reviews():
    reviews = list(db.member.find({},{'_id':0,'id':1,'pw':1}))
    return jsonify({'all_reviews' : reviews})

@app.route('/reviews', methods=['POST'])
def write_review2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.review.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/rv', methods=['GET'])
def read_reviews2():
    rv = list(db.review.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/rank', methods=['GET'])
def read_rank():
    avrank = list(db.review.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#액션5
@app.route('/action5', methods=['POST'])
def write_action5():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.action5.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/action5-1', methods=['GET'])
def read_action5():
    rv = list(db.action5.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/action5-rank', methods=['GET'])
def read_rankaction5():
    avrank = list(db.action5.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#액션4
@app.route('/action4', methods=['POST'])
def write_action4():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.action4.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/action4-1', methods=['GET'])
def read_action4():
    rv = list(db.action4.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/action4-rank', methods=['GET'])
def read_rankaction4():
    avrank = list(db.action4.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#액션1
@app.route('/action1', methods=['POST'])
def write_action1():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.action1.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/action1-1', methods=['GET'])
def read_action1():
    rv = list(db.action1.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/action1-rank', methods=['GET'])
def read_rankaction1():
    avrank = list(db.action1.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#액션3
@app.route('/action3', methods=['POST'])
def write_action3():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.action3.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/action3-1', methods=['GET'])
def read_action3():
    rv = list(db.action3.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/action3-rank', methods=['GET'])
def read_rankaction3():
    avrank = list(db.action3.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#액션2
@app.route('/action2', methods=['POST'])
def write_action2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.action2.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/action2-1', methods=['GET'])
def read_action2():
    rv = list(db.action2.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/action2-rank', methods=['GET'])
def read_rankaction2():
    avrank = list(db.action2.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#애니5
@app.route('/ani5', methods=['POST'])
def write_ani5():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.ani5.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/ani5-1', methods=['GET'])
def read_ani5():
    rv = list(db.ani5.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/ani5-rank', methods=['GET'])
def read_rankani5():
    avrank = list(db.ani5.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#애니4
@app.route('/ani4', methods=['POST'])
def write_ani4():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.ani4.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/ani4-1', methods=['GET'])
def read_ani4():
    rv = list(db.ani4.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/ani4-rank', methods=['GET'])
def read_rankani4():
    avrank = list(db.ani4.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#애니1
@app.route('/ani1', methods=['POST'])
def write_ani1():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.ani1.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/ani1-1', methods=['GET'])
def read_ani1():
    rv = list(db.ani1.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/ani1-rank', methods=['GET'])
def read_rankani1():
    avrank = list(db.ani1.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#애니3
@app.route('/ani3', methods=['POST'])
def write_ani3():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.ani3.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/ani3-1', methods=['GET'])
def read_ani3():
    rv = list(db.ani3.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/ani3-rank', methods=['GET'])
def read_rankani3():
    avrank = list(db.ani3.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#애니2
@app.route('/ani2', methods=['POST'])
def write_ani2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.ani2.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/ani2-1', methods=['GET'])
def read_ani2():
    rv = list(db.ani2.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/ani2-rank', methods=['GET'])
def read_rankani2():
    avrank = list(db.ani2.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#코미디5
@app.route('/comedy5', methods=['POST'])
def write_comedy5():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.comedy5.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/comedy5-1', methods=['GET'])
def read_comedy5():
    rv = list(db.comedy5.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/comedy5-rank', methods=['GET'])
def read_rankcomedy5():
    avrank = list(db.comedy5.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})



#코미디4
@app.route('/comedy4', methods=['POST'])
def write_comedy4():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.comedy4.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/comedy4-1', methods=['GET'])
def read_comedy4():
    rv = list(db.comedy4.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/comedy4-rank', methods=['GET'])
def read_rankcomedy4():
    avrank = list(db.comedy4.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#코미디1
@app.route('/comedy1', methods=['POST'])
def write_comedy1():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.comedy1.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/comedy1-1', methods=['GET'])
def read_comedy1():
    rv = list(db.comedy1.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/comedy1-rank', methods=['GET'])
def read_rankcomedy1():
    avrank = list(db.comedy1.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#코미디3
@app.route('/comedy3', methods=['POST'])
def write_comedy3():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.comedy3.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/comedy3-1', methods=['GET'])
def read_comedy3():
    rv = list(db.comedy3.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/comedy3-rank', methods=['GET'])
def read_rankcomedy3():
    avrank = list(db.comedy3.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#코미디2
@app.route('/comedy2', methods=['POST'])
def write_comedy2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.comedy2.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/comedy2-1', methods=['GET'])
def read_comedy2():
    rv = list(db.comedy2.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/comedy2-rank', methods=['GET'])
def read_rankcomedy2():
    avrank = list(db.comedy2.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#로맨스5
@app.route('/romence5', methods=['POST'])
def write_romence5():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.romence5.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/romence5-1', methods=['GET'])
def read_romence5():
    rv = list(db.romence5.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/romence5-rank', methods=['GET'])
def read_rankromence5():
    avrank = list(db.romence5.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})

#로맨스4
@app.route('/romence4', methods=['POST'])
def write_romence4():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.romence4.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/romence4-1', methods=['GET'])
def read_romence4():
    rv = list(db.romence4.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/romence4-rank', methods=['GET'])
def read_rankromence4():
    avrank = list(db.romence4.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#로맨스1
@app.route('/romence1', methods=['POST'])
def write_romence1():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.romence1.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/romence1-1', methods=['GET'])
def read_romence1():
    rv = list(db.romence1.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/romence1-rank', methods=['GET'])
def read_rankromence1():
    avrank = list(db.romence1.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


#로맨스3
@app.route('/romence3', methods=['POST'])
def write_romence3():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.romence3.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/romence3-1', methods=['GET'])
def read_romence3():
    rv = list(db.romence3.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/romence3-rank', methods=['GET'])
def read_rankromence3():
    avrank = list(db.romence3.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})




#로맨스2
@app.route('/romence2', methods=['POST'])
def write_romence2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.romence2.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/romence2-1', methods=['GET'])
def read_romence2():
    rv = list(db.romence2.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/romence2-rank', methods=['GET'])
def read_rankromence2():
    avrank = list(db.romence2.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})



#스릴러5
@app.route('/thriller5', methods=['POST'])
def write_thriller5():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.thriller5.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/thriller5-1', methods=['GET'])
def read_thriller5():
    rv = list(db.thriller5.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/thriller5-rank', methods=['GET'])
def read_rankthriller5():
    avrank = list(db.thriller5.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})




#스릴러4
@app.route('/thriller4', methods=['POST'])
def write_thriller4():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.thriller4.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/thriller4-1', methods=['GET'])
def read_thriller4():
    rv = list(db.thriller4.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/thriller4-rank', methods=['GET'])
def read_rankthriller4():
    avrank = list(db.thriller4.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})




#스릴러1
@app.route('/thriller1', methods=['POST'])
def write_thriller1():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.thriller1.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/thriller1-1', methods=['GET'])
def read_thriller1():
    rv = list(db.thriller1.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/thriller1-rank', methods=['GET'])
def read_rankthriller1():
    avrank = list(db.thriller1.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})




#스릴러3
@app.route('/thriller3', methods=['POST'])
def write_thriller3():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.thriller3.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/thriller3-1', methods=['GET'])
def read_thriller3():
    rv = list(db.thriller3.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/thriller3-rank', methods=['GET'])
def read_rankthriller3():
    avrank = list(db.thriller3.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})




#스릴러2
@app.route('/thriller2', methods=['POST'])
def write_thriller2():
    review_receive = request.form.get('review_give',False)
    result_receive = request.form.get('result_give',False)
    rank_receive = request.form.get('rank_give',False)
    dateString_receive = request.form.get('dateString_give',False)


    doc = {
        'review': review_receive,
        'result': result_receive,
        'rank': rank_receive,
        'dateString': dateString_receive
    }

    db.thriller2.insert_one(doc)

    return jsonify({'msg': '리뷰 작성 완료!'})

@app.route('/thriller2-1', methods=['GET'])
def read_thriller2():
    rv = list(db.thriller2.find({}, {'_id': False}))
    return jsonify({'all_reviews': rv})

@app.route('/thriller2-rank', methods=['GET'])
def read_rankthriller2():
    avrank = list(db.thriller2.find({},{'_id':False}))
    return jsonify({'all_rank' : avrank})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
