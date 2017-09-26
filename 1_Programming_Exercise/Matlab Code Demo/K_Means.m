function [class, cent] = K_Means(x, k, max_iter)
% *********************************************************************** %
% K-Means Clustering Algorithm [Lloyd' K-Means].
% --------
% INPUT  :
% --------
%   x    : matrix(point_num, dimension_num), Double
%          point set
%   k    : matrix(1, 1), Integer
%          total number of centroids
%   max_iter : matrix(1, 1), Integer
%          maximum number of iterations
% --------
% OUTPUT :
% --------
%   class: matrix(point_num, 1), Integer
%          range from 1 to k
%   cent : matrix(k, dimension_num), Double
% --------
% Example:
% --------
%     rng(1);
%     x = [mvnrnd([5 5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([5 -5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([-5 5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([-5 -5], [1.5 0; 0 1.5], 500)];
%     k = 4;
%     [class, cent] = K_Means(x, k, 1e3);
%     fig_colors = {'r', 'b', 'g', 'm'};
%     for k_ind = 1 : k
%         plot(x(class == k_ind, 1), x(class == k_ind, 2), '.', 'Color', fig_colors{1, k_ind}); hold on;
%         plot(cent(k_ind, 1), cent(k_ind, 2), 'kx', 'MarkerSize', 12, 'LineWidth', 5); 
%     end
%     hold off;
% --------
% Ref    :
% --------
%   * Lloyd S. Least squares quantization in PCM. 
%       IEEE transactions on information theory. 1982 Mar;28(2):129-37.
%   * http://lear.inrialpes.fr/~verbeek/software
% *********************************************************************** %
    [point_num, ~] = size(x);
    cent = x(randperm(point_num, k), :);
    for iter_ind = 1 : max_iter
        dist = pdist2(x, cent);
        [~, class] = min(dist, [], 2);
        for cent_ind = 1 : k
            cent(cent_ind, :) = mean(x(class == cent_ind, :), 1);
        end
    end
end
