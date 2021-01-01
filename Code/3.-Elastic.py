import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

from sklearn. model_selection import train_test_split
from sklearn.metrics import mean_squared_error


if __name__ == "__main__":
    dataset = pd.read_csv('./data/whr2017.csv')
    # print(dataset.describe())

    X = dataset[['gdp', 'family', 'lifexp', 'freedom',
                 'corruption', 'generosity', 'dystopia']]
    y = dataset[['score']] 

    # print(X.shape)
    # print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    modelLinear = LinearRegression().fit(X_train, y_train)
    y_pred_linear = modelLinear.predict(X_test)

    modelLasso = Lasso(alpha=0.02).fit(X_train, y_train)
    y_pred_lasso = modelLasso.predict(X_test)

    modelRidge = Ridge(alpha=1).fit(X_train, y_train)
    y_pred_ridge = modelRidge.predict(X_test)

    modelElasticNet = ElasticNet(random_state=0).fit(X_train, y_train)
    y_pred_elastic = modelElasticNet.predict(X_test)

    linear_loss = mean_squared_error(y_test, y_pred_linear)
    print('Linear Loss: ', linear_loss)

    lasso_loss = mean_squared_error(y_test, y_pred_lasso)
    print('Lasso Loss: ', lasso_loss)

    ridge_loss = mean_squared_error(y_test, y_pred_ridge)
    print('Ridge Loss: ', ridge_loss)

    elastic_loss = mean_squared_error(y_test, y_pred_elastic)
    print('ElasticNet Loss: ', elastic_loss)

    print('='*32, '\n')
    print("Coef Linear: ", modelLinear.coef_)
    print("Coef Lasso: ", modelLasso.coef_)
    print("Coef Ridge: ", modelRidge.coef_)
    print("Coef Elastic: ", modelElasticNet.coef_)