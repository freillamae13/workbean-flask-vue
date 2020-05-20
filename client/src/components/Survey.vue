<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Surveys</h1>
        <hr><br><br>
        <notice :message="message" v-if="showMessage"></notice>
        <button type="button"
          class="btn btn-success btn-sm"
          v-b-modal.survey-modal>Add Survey</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Profile Image</th>
              <th scope="col">Full Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Gender</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(survey, index) in surveys" :key="index">
              <td>{{ survey.profile }}</td>
              <td>{{ survey.firstname }}</td>
              <td>{{ survey.lastname }}</td>
              <td>{{ survey.gender }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.survey-update-modal
                          @click="editSurvey(survey)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSurvey(survey)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addSurveyModal" id="survey-modal" title="Add a new survey" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-profile-group" label="Profile:" label-for="form-profile-upload">
          <b-form-file
            id="form-profile-upload"
            v-model="addSurveyForm.profile"
            :state="Boolean(file)"
            accept=".jpg, .png, .gif"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-form-group>
        <b-form-group id="form-firstname-group" label="Firstname:" label-for="form-firstname-input">
          <b-form-input id="form-firstname-input"
            type="text"
            v-model="addSurveyForm.firstname"
            required
            placeholder="Enter firstname">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-lastname-group" label="Lastname:" label-for="form-lastname-input">
          <b-form-input id="form-lastname-input"
            type="text"
            v-model="addSurveyForm.lastname"
            required
            placeholder="Enter lastname">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Gender">
          <b-form-radio
            v-model="addSurveyForm.gender"
            name="gender"
            value="Female">Female</b-form-radio>
          <b-form-radio
            v-model="addSurveyForm.gender"
            name="gender"
            value="Male">Male</b-form-radio>
        </b-form-group>
        <b-form-group label="Favorite Programming Language:">
          <b-form-checkbox-group
            id="form-favorite-checkbox"
            v-model="addSurveyForm.favorite"
            name="favorite">
              <b-form-checkbox value="PHP">PHP</b-form-checkbox>
              <b-form-checkbox value="Python">Python</b-form-checkbox>
              <b-form-checkbox value="Go">Go</b-form-checkbox>
              <b-form-checkbox value="Ruby">Ruby</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-form-group
          id="form-favorite_why-group"
          label="Why do you like that language?"
          label-for="form-favorite_why-textarea">
          <b-form-textarea
            id="form-favorite_why-textarea"
            placeholder="Write your answer here..."
            v-model="addSurveyForm.favorite_why"
            rows="8"
          ></b-form-textarea>
        </b-form-group>
        <b-form-group
          id="python-rating-group"
          label="Rate Python:"
          label-for="python-rating">
          <b-form-rating
            id="python-rating"
            v-model="addSurveyForm.python"
            stars="10"></b-form-rating>
          <p class="mt-2">Value: {{ addSurveyForm.python }}</p>
        </b-form-group>
        <b-form-group
          id="php-rating-group"
          label="Rate PHP:"
          label-for="php-rating">
          <b-form-rating id="php-rating" v-model="addSurveyForm.php" stars="5"></b-form-rating>
          <p class="mt-2">Value: {{ addSurveyForm.php }}</p>
        </b-form-group>
        <b-form-group
          id="form-favorite_questions-group"
          label="Any more questions?"
          label-for="form-favorite_questions-textarea">
          <b-form-textarea
            id="form-favorite_questions-textarea"
            v-model="addSurveyForm.questions"
            placeholder="Write your questions here..."
            rows="4"
          ></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editSurveyModal" id="survey-update-modal" title="Update" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group
          id="form-profile-edit-group"
          label="Profile:"
          label-for="form-profile-edit-upload">
          <b-form-file
            id="form-profile-edit-upload"
            v-model="editForm.profile"
            :state="Boolean(file)"
            accept=".jpg, .png, .gif"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-form-group>
        <b-form-group
          id="form-firstname-edit-group"
          label="Firstname:"
          label-for="form-firstname-edit-input">
          <b-form-input id="form-firstname-edit-input"
            type="text"
            v-model="editForm.firstname"
            required
            placeholder="Enter firstname">
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-lastname-edit-group"
          label="Lastname:"
          label-for="form-lastname-edit-input">
          <b-form-input id="form-lastname-edit-input"
            type="text"
            v-model="editForm.lastname"
            required
            placeholder="Enter lastname">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Gender">
          <b-form-radio
            v-model="editForm.gender"
            name="gender"
            value="Female">Female</b-form-radio>
          <b-form-radio
            v-model="editForm.gender"
            name="gender"
            value="Male">Male</b-form-radio>
        </b-form-group>
        <b-form-group label="Favorite Programming Language:">
          <b-form-checkbox-group
            id="form-favorite-edit-checkbox"
            v-model="editForm.favorite"
            name="favorite">
              <b-form-checkbox value="PHP">PHP</b-form-checkbox>
              <b-form-checkbox value="Python">Python</b-form-checkbox>
              <b-form-checkbox value="Go">Go</b-form-checkbox>
              <b-form-checkbox value="Ruby">Ruby</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-form-group
          id="form-favorite_why-edit-group"
          label="Why do you like that language?"
          label-for="form-favorite_why-edit-textarea">
          <b-form-textarea
            id="form-favorite_why-edit-textarea"
            placeholder="Write your answer here..."
            v-model="editForm.favorite_why"
            rows="8"
          ></b-form-textarea>
        </b-form-group>
        <b-form-group
          id="python-rating-edit-group"
          label="Rate Python:"
          label-for="python-rating-edit">
          <b-form-rating
            id="python-rating-edit"
            v-model="editForm.python"
            stars="10"></b-form-rating>
          <p class="mt-2">Value: {{ editForm.python }}</p>
        </b-form-group>
        <b-form-group
          id="php-rating-edit-group"
          label="Rate PHP:"
          label-for="php-rating-edit">
          <b-form-rating id="php-rating-edit" v-model="editForm.php" stars="5"></b-form-rating>
          <p class="mt-2">Value: {{ editForm.php }}</p>
        </b-form-group>
        <b-form-group
          id="form-favorite_questions-edit-group"
          label="Any more questions?"
          label-for="form-favorite_questions-edit-textarea">
          <b-form-textarea
            id="form-favorite_questions-edit-textarea"
            v-model="editForm.questions"
            placeholder="Write your questions here..."
            rows="4"
          ></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Notice from './Notice.vue';

export default {
  data() {
    return {
      value10: null,
      value5: null,
      surveys: [],
      addSurveyForm: {
        profile: '',
        firstname: '',
        lastname: '',
        gender: '',
        favorite: '',
        favorite_why: '',
        php: '',
        python: '',
        questions: '',
      },
      editForm: {
        id: '',
        profile: '',
        firstname: '',
        lastname: '',
        gender: '',
        favorite: '',
        favorite_why: '',
        php: '',
        python: '',
        questions: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    notice: Notice,
  },
  methods: {
    getSurveys() {
      const path = 'http://localhost:5000/api/surveys';
      axios.get(path)
        .then((res) => {
          this.surveys = res.data.surveys;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addSurvey(payload) {
      const path = 'http://localhost:5000/api/surveys';
      axios.post(path, payload)
        .then(() => {
          this.getSurveys();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSurveys();
        });
    },
    updateSurvey(payload, surveyID) {
      const path = `http://localhost:5000/api/surveys/${surveyID}`;
      axios.put(path, payload)
        .then(() => {
          this.getSurveys();
          this.message = 'Survey updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSurveys();
        });
    },
    editSurvey(survey) {
      this.editForm = survey;
    },
    initForm() {
      this.addSurveyForm.profile = '';
      this.addSurveyForm.firstname = '';
      this.addSurveyForm.lastname = '';
      this.addSurveyForm.gender = '';
      this.addSurveyForm.favorite = '';
      this.addSurveyForm.favorite_why = '';
      this.addSurveyForm.php = '';
      this.addSurveyForm.python = '';
      this.addSurveyForm.questions = '';
      this.editForm.id = '';
      this.editForm.profile = '';
      this.editForm.firstname = '';
      this.editForm.lastname = '';
      this.editForm.gender = '';
      this.editForm.favorite = '';
      this.editForm.favorite_why = '';
      this.editForm.php = '';
      this.editForm.python = '';
      this.editForm.questions = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSurveyModal.hide();
      const payload = {
        profile: this.addSurveyForm.profile,
        firstname: this.addSurveyForm.firstname,
        lastname: this.addSurveyForm.lastname,
        gender: this.addSurveyForm.gender,
        favorite: this.addSurveyForm.favorite,
        favorite_why: this.addSurveyForm.favorite_why,
        php: this.addSurveyForm.php,
        python: this.addSurveyForm.python,
        questions: this.addSurveyForm.questions,
      };
      this.addSurvey(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSurveyModal.hide();
      const payload = {
        profile: this.editForm.profile,
        firstname: this.editForm.firstname,
        lastname: this.editForm.lastname,
        gender: this.editForm.gender,
        favorite: this.editForm.favorite,
        favorite_why: this.editForm.favorite_why,
        php: this.editForm.php,
        python: this.editForm.python,
        questions: this.editForm.questions,
      };
      this.updateSurvey(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSurveyModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSurveyModal.hide();
      this.initForm();
      this.getSurveys(); // why?
    },
    removeSurvey(surveyID) {
      const path = `http://localhost:5000/api/surveys/${surveyID}`;
      axios.delete(path)
        .then(() => {
          this.getSurveys();
          this.message = 'Survey removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSurveys();
        });
    },
    onDeleteSurvey(survey) {
      this.removeSurvey(survey.id);
    },
  },
  created() {
    this.getSurveys();
  },
};
</script>
