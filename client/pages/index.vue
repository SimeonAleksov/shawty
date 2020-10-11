<template>
  <v-layout>
  <v-container>
    <v-row
      justify="space-between"
    >
      <v-col
        cols="2"
        md="5"
      >
        <v-form ref="form">
          <v-text-field
            :counter="max"
            :rules="rules"
            label="URL"
            placeholder="Your URL here"
          ></v-text-field>
                  <v-slider
          v-model="max"
          label="Max characters"
        >
        </v-slider>
          <v-btn
            @click="createURL()"
            color="accent"
            depressed
            elevation="2"
            large
            medium
            raised
            rounded>
            Generate
          </v-btn>
        </v-form>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
      </v-col>
    </v-row>
  </v-container>
  </v-layout>
</template>

<script>
  import gql from 'graphql-tag'
  export default {
    apollo: {
      urls: gql`
      query {
        urls {
          fullUrl
          urlHash
        }
      }
      `
    },
    data: () => ({
      allowSpaces: false,
      max: 5,
    }),
    computed: {
      rules () {
        const rules = [];

        if (this.max) {
          const rule =
            v => (v || '').length <= this.max ||
              `A maximum of ${this.max} characters is allowed`;
          rules.push(rule)
        }
        return rules
      },
    },

    watch: {
      match: 'validateField',
      max: 'validateField',
    },

    methods: {
      validateField () {
        this.$refs.form.validate()
      },
      async createURL() {
        const query = "query {\n" +
          "  urls {\n" +
          "    fullUrl\n" +
          "    urlHash\n" +
          "  }\n" +
          "}";
        console.log(query);
        const response = await this.$axios.$post('/graphql/', { query });
        console.log(response)
      },
    },
  }
</script>
