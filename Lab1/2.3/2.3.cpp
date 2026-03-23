#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <random>
#include <cmath>
#include <cctype>

using namespace std;

string clean_text(const string &text) {
    string result;
    for (char c : text) {
        if (isalpha(c))
            result += toupper(c);
    }
    return result;
}

unordered_map<string, double> build_trigram_model(const string &reference_text) {
    string text = clean_text(reference_text);

    unordered_map<string, int> counts;
    unordered_map<string, double> model;

    int total = 0;

    for (size_t i = 0; i + 2 < text.size(); i++) {
        string tg = text.substr(i, 3);
        counts[tg]++;
        total++;
    }

    for (auto &p : counts) {
        model[p.first] = log10((double)p.second / total);
    }

    return model;
}

string decrypt(const string &ciphertext, const string &key) {
    string result = ciphertext;

    for (char &c : result) {
        if (isupper(c))
            c = key[c - 'A'];
        else if (islower(c))
            c = tolower(key[c - 'a']);
    }

    return result;
}

double calculate_fitness(const string &text,
                         const unordered_map<string, double> &model) {

    double score = 0;

    for (size_t i = 0; i + 2 < text.size(); i++) {
        string tg = text.substr(i, 3);

        auto it = model.find(tg);
        if (it != model.end())
            score += it->second;
        else
            score += -15.0;
    }

    return score;
}

string random_key(mt19937 &rng) {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    shuffle(alphabet.begin(), alphabet.end(), rng);
    return alphabet;
}

string hill_climbing(const string &ciphertext,
                     const unordered_map<string, double> &model,
                     int max_restarts = 15) {

    random_device rd;
    mt19937 rng(rd());

    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    string best_key;
    double best_score = -1e18;

    cout << "Analyzing ciphertext...\n\n";

    for (int r = 0; r < max_restarts; r++) {

        string current_key = random_key(rng);
        double current_score =
            calculate_fitness(decrypt(ciphertext, current_key), model);

        bool improvement = true;

        while (improvement) {

            improvement = false;

            for (int i = 0; i < 25; i++) {
                for (int j = i + 1; j < 26; j++) {

                    string test_key = current_key;
                    swap(test_key[i], test_key[j]);

                    double test_score =
                        calculate_fitness(decrypt(ciphertext, test_key), model);

                    if (test_score > current_score) {
                        current_score = test_score;
                        current_key = test_key;
                        improvement = true;
                    }
                }
            }
        }

        if (current_score > best_score) {
            best_score = current_score;
            best_key = current_key;
        }
    }

    return best_key;
}

int main() {

    string reference_text =
        "Cryptography is the practice and study of techniques for secure "
        "communication in the presence of adversarial behavior. "
        "More generally cryptography is about constructing protocols that "
        "prevent third parties from reading private messages.";

    auto trigram_model = build_trigram_model(reference_text);

    string ciphertext = R"(Max NBM bl t extwbgz bglmbmnmbhg ngwxk OGN-AVF...)";

    string clean_cipher = clean_text(ciphertext);

    string best_key = hill_climbing(clean_cipher, trigram_model, 10);

    string plaintext = decrypt(ciphertext, best_key);

    cout << "====================================\n";
    cout << "KEY: " << best_key << endl;
    cout << "====================================\n";
    cout << plaintext << endl;
}