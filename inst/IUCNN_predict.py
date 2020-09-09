def iucnn_predict(feature_set,model_dir,
                  verbose=0,
                  return_prob=False):
    print("Loading model...")
    model = tf.keras.models.load_model(model_dir)
    prm_est = model.predict(feature_set, verbose=verbose)
    predictions = np.argmax(prm_est, axis=1)
    if return_prob:
        return [predictions, prm_est]
    else:
        return [predictions]